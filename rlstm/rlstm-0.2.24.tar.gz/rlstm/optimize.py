"""
Similar file to early_stopping/optimize.py but
depends on converging vs early_stopping
"""

from __future__ import absolute_import

import autograd.numpy as np
from autograd.util import flatten_func
from builtins import range
from random import sample
from math import ceil
from copy import copy
import pdb


def adam(
        grad,
        init_params,
        num_batches=1,
        callback=None,
        min_epoch=1,
        max_epoch=20,
        step_size=0.001,
        b1=0.9,
        b2=0.999,
        eps=10**-8,
        ll_fun=None,
        err_fun=None,
        va_ll_fun=None,
        va_err_fun=None,
        stop_criterion=1e-3,
        early_stop=False,
        patience=10):
    """ Adam as described in http://arxiv.org/pdf/1412.6980.pdf.
    It's basically RMSprop with momentum and some correction terms."""

    flattened_grad, unflatten, x = flatten_func(grad, init_params)

    # initial settings for variables
    m, v = np.zeros(len(x)), np.zeros(len(x))
    reset_patience = patience

    # initialize loglikelihoods (these are used to determine convergence)
    # we define a single ll per batch so we know which to compare to.
    # Comparing ll between batches doesn't make sense.
    old_ll, cur_ll = np.ones(num_batches), np.zeros(num_batches)
    cur_va_ll, best_va_ll = None, None

    cur_err = np.zeros(num_batches)
    cur_va_err = None

    # training goes until all batches have converged / max_iter
    have_converged = np.zeros(num_batches)

    cur_iter = 0  # != epoch
    cur_batch = 0
    cur_epoch = 0

    while (cur_epoch < max_epoch) or (cur_epoch < min_epoch):
        # we can test convergence for every batch and keep track
        # of which batches have converged
        if (np.abs(cur_ll[cur_batch] - old_ll[cur_batch]) <= stop_criterion):
            have_converged[cur_batch] = 1
        else:  # this should rarely fire
            have_converged[cur_batch] = 0

        # if all batches have converged before max_iter: break
        if sum(have_converged) == num_batches:
            break

        # pdb.set_trace()
        g = flattened_grad(x, cur_iter)  # pass iter for batch training
        m = (1 - b1) * g + b1 * m  # First  moment estimate.
        v = (1 - b2) * (g**2) + b2 * v  # Second moment estimate.
        mhat = m / (1 - b1**(cur_iter + 1))    # Bias correction.
        vhat = v / (1 - b2**(cur_iter + 1))
        x = x - step_size*mhat/(np.sqrt(vhat) + eps)

        if ll_fun:
            old_ll[cur_batch] = cur_ll[cur_batch]
            cur_ll[cur_batch] = ll_fun(x, cur_iter)

        if err_fun:
            cur_err[cur_batch] = err_fun(x, cur_iter)

        if va_ll_fun and cur_batch == num_batches - 1:
            cur_va_ll = va_ll_fun(x)

            # stop based on va ll
            if early_stop:
                if cur_epoch == 0:
                    best_va_ll = cur_va_ll
                    best_x = x
                else:
                    if cur_va_ll <= best_va_ll:
                        best_va_ll = cur_va_ll
                        best_x = x
                        patience = reset_patience
                    else:
                        patience -= 1

                if patience <= 0:
                    break

            if va_err_fun:
                cur_va_err = va_err_fun(x)

        if callback:
            callback(cur_epoch,
                     cur_batch,
                     np.sum(cur_ll[:cur_batch+1]),
                     np.mean(cur_err[:cur_batch+1]),
                     cur_va_ll,
                     cur_va_err,
                     x)

        cur_iter += 1
        cur_batch = cur_iter % num_batches
        cur_epoch = cur_iter // num_batches

    return unflatten(best_x if early_stop else x)
