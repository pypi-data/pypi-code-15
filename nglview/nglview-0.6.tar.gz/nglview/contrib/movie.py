import os
import time
import moviepy.editor as mpy
import threading

class MovieMaker(object):
    """

    Parameters
    ----------
    view : NGLWidget
    download_folder : str or None
        Folder that stores images. You can not arbitarily set this folder. It must be
        the download directory of the web browser you are using.
        If None, $HOME/Downloads/ will be used.
    prefix : str, default 'movie'
        prefix name of rendered image.
    output : str, default 'my_movie.gif'
        output filename of the movie.
        if output has '.gif', call `write_gif`, otherwise calling `write_videofile`
    fps : 8
        frame per second
    start, stop, step : int, default (0, -1, 1)
        how many frames you want to render.
    skip_render : bool, default False
        if True, do not render any frame and uses existings images in `download_folder`
        for movie making.
        if False, perform rendering first.
    timeout : a number (second), default 1.
        The waiting time between rendering two consecutive frames.
        You need to decide the "good" value by your self. `timeout` should be larger than
        the rendering time of each frame.
    render_params : dict or None, default None
        NGL rendering params. see NGLWidget.download_image.
        If None, use default values
    mpy_params : dict or None, default None
        moviepy params for `write_gif` method.
        if None, use default values
    in_memory : bool, default False
        if False, save rendered images to disk first
        if True, keep all image data in memory (good for small video)

    Examples
    --------
    >>> import nglview as nv
    >>> import pytraj as pt
    >>> traj = pt.load(nv.datafiles.XTC, top=nv.datafiles.PDB)
    >>> view = nv.show_pytraj(traj)
    >>> from nglview.contrib.movie import MovieMaker
    >>> download_folder = '/Users/xxx/Downloads'
    >>> output = 'my.gif'
    >>> mov = MovieMaker(view, download_folder=download_folder, output=output)
    >>> mov.make()

    >>> # write avi format
    >>> from nglview.contrib.movie import MovieMaker

    >>> mpy_params = {
    ...     'codec': 'mpeg4'
    ... }
    >>> movie = MovieMaker(view, output='my.avi', in_memory=True, mpy_params=mpy_params)
    >>> movie.make()

    Notes
    -----
    unstable API. Currently supports .gif format
    If you are using remote notebook, make sure to set in_memory=True

    Requires
    --------
    
    moviepy. e.g:
    
        pip install moviepy
        conda install freeimage

    """
    
    def __init__(self,
                 view,
                 download_folder=None,
                 prefix='movie',
                 output='my_movie.gif',
                 fps=8,
                 start=0,
                 stop=-1,
                 step=1,
                 skip_render=False,
                 timeout=1.,
                 in_memory=False,
                 render_params=None,
                 mpy_params=None):
        if download_folder is None:
            download_folder = os.getenv('HOME', '') + '/Downloads/'
        self.view = view
        self.skip_render = skip_render
        self.prefix = prefix
        self.download_folder = download_folder
        self.timeout = timeout
        self.fps = fps
        self.in_memory = in_memory
        self.render_params = render_params if render_params is not None else {}
        self.mpy_params = mpy_params if mpy_params is not None else {}
        if self.render_params is not None:
            assert isinstance(self.render_params, dict)
        if self.mpy_params is not None:
            assert isinstance(self.mpy_params, dict)
        self.output = output
        if stop < 0:
            stop = self.view.count
        self._time_range = range(start, stop, step)
        self._event = threading.Event()
        self._thread = None
        self._image_array = []

    def make(self, in_memory=False):
        # TODO : make base class so we can reuse this with sandbox/base.py
        self._event = threading.Event()

        def _make(event):
            if not self.skip_render:
                for i in self._time_range:
                    if not event.is_set():
                        self.view.frame = i
                        time.sleep(self.timeout)
                        if not self.in_memory:
                            self.view.download_image(self.prefix + '.' + str(i) + '.png',
                                    **self.render_params)
                        else:
                            self.view.render_image(**self.render_params)
                        time.sleep(self.timeout)
                        if self.in_memory:
                            rgb = self._base64_to_ndarray(self.view._image_data)
                            self._image_array.append(rgb)
                if not self.in_memory:
                    template = "{}/{}.{}.png"
                    image_files = [image_dir for image_dir in 
                                      (template.format(self.download_folder,
                                                               self.prefix,
                                                               str(i))
                                       for i in self._time_range)
                                   if os.path.exists(image_dir)]
                else:
                    image_files = self._image_array
            if not self._event.is_set():
                clip = mpy.ImageSequenceClip(image_files, fps=self.fps)
                if self.output.endswith('.gif'):
                    clip.write_gif(self.output, fps=self.fps, **self.mpy_params)
                else:
                    clip.write_videofile(self.output, fps=self.fps, **self.mpy_params)
                self._image_array = []
        self.thread = threading.Thread(target=_make, args=(self._event,))
        self.thread.daemon = True
        self.thread.start()

    def interupt(self):
        """ Stop making process """
        if self._event is not None:
            self._event.set()

    def _base64_to_ndarray(self, value):
        import io
        import base64
        import matplotlib.image as mpimg
        im_bytes = base64.b64decode(value)
        im_bytes = io.BytesIO(im_bytes)
        # convert to numpy RGB value (for moviepy.editor.VideoClip)
        return mpimg.imread(im_bytes, format='JPG')
