#!/usr/bin/env python3

from copy import deepcopy
import logging
import os
import hashlib
import pickle

from pymediainfo import MediaInfo
from tqdm import tqdm

from .cprint import cprint
from .misc import getVideosInFileList, getTrackQuality

log = logging.getLogger()

def _pruneMissingFromFileMap(fileMap):
    cprint("blue", "Checking for missing/deleted files...")
    tempMap = deepcopy(fileMap)
    collection = tempMap
    if log.level > logging.INFO:
        collection = tqdm(tempMap)
    for dirPath in collection:
        if not os.path.exists(dirPath):
            log.info("Removing %s from cache" % dirPath)
            del fileMap[dirPath]
            continue

        for video in tempMap[dirPath]:
            videoPath = os.path.join(dirPath, video)
            if not os.path.exists(videoPath):
                log.info("Removing %s from cache" % videoPath)
                del fileMap[dirPath][video]
    return fileMap

def _videoInCache(video, dirPath, fileMap):
    if video in fileMap[dirPath]:
        log.debug("Found %s in cache..." % video)
        videoPath = os.path.join(dirPath, video)
        videoSize = os.stat(videoPath).st_size
        if fileMap[dirPath][video]["size"] == videoSize and fileMap[dirPath][video]["quality"] != 'Unknown':
            log.info("Using cache for %s" % video)
            return True
        log.debug("Filesize differs. Invalidating cache")
    return False


def _getVideoMetadata(videoPath):
    rawMetadata = MediaInfo.parse(videoPath)
    outputMetadata = {}
    outputMetadata["size"] = os.stat(videoPath).st_size
    for track in rawMetadata.tracks:
        if track.track_type == "Video":
            outputMetadata["quality"] = getTrackQuality(track)
            outputMetadata["format"] = track.format
            break
    return outputMetadata


def _updateFileMap(directory, fileMap):
    fileMap = _pruneMissingFromFileMap(fileMap)
    for dirPath, dirNames, fileNames in os.walk(directory, followlinks=True):
        cprint("green", "Working in directory: %s" % dirPath)

        videos = getVideosInFileList(fileNames)
        log.info("Total videos in %s: %s" % (dirPath, len(videos)))

        if log.level > logging.INFO:
            videos = tqdm(videos)
        changes = False
        for video in videos:
            if dirPath not in fileMap:  # Only create if there are videos for this path
                fileMap[dirPath] = {}
            if _videoInCache(video, dirPath, fileMap):
                continue

            changes = True
            log.info("Parsing %s" % video)
            videoPath = os.path.join(dirPath, video)
            fileMap[dirPath][video] = _getVideoMetadata(videoPath)

        if changes:
            _saveCachedFileMap(directory, fileMap)
    return fileMap


def _getFileMapPicklePath(directory):
    picklePath = os.path.join(os.path.expanduser("~"), ".video_utils")
    fileMapName = hashlib.md5(bytes(directory, 'ascii')).hexdigest()
    fileMapPicklePath = os.path.join(picklePath, fileMapName)
    return fileMapPicklePath


def _saveCachedFileMap(directory, fileMap):
    log.info("Saving out filemap...")
    fileMapPicklePath = _getFileMapPicklePath(directory)
    picklePath = os.path.dirname(fileMapPicklePath)
    if not os.path.exists(picklePath):
        os.mkdir(picklePath)
    with open(fileMapPicklePath, 'wb') as f:
        pickle.dump(fileMap, f)


def _loadCachedFileMap(directory):
    fileMapPicklePath = _getFileMapPicklePath(directory)

    fileMap = {}
    if os.path.exists(fileMapPicklePath):
        log.info("Loading from cache...")
        with open(fileMapPicklePath, 'rb') as f:
            fileMap = pickle.load(f)

    return fileMap


def getFileMap(directory, update=True, useCache=True):
    fileMap = {}
    directory = os.path.realpath(directory)

    if not useCache and not update:
        raise Exception("At least one of update or useCache must be True")

    if useCache:
        fileMap = _loadCachedFileMap(directory)

    if update:
        fileMap = _updateFileMap(directory, fileMap)

    return fileMap
