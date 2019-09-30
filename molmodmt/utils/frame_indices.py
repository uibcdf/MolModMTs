
def digest(item, frame_indices):

    from numpy import arange, array
    from molmodmt.multitool import get_form
    from molmodmt.multitool import _dict_get

    if frame_indices is None:
        n_frames = 0
        frame_indices = arange(n_frames, dtype='int64')
    elif type(frame_indices)==int:
        frame_indices = array([frame_indices], dtype='int64')
    elif type(frame_indices)==str:
        if frame_indices == 'all':
            in_form = get_form(item)
            n_frames = _dict_get[in_form]['system']['n_frames'](item)
            frame_indices = arange(n_frames, dtype='int64')

    return frame_indices

