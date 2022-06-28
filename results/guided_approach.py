import cv2

def guided_depth_map_fill(depth_map, guide_image):
    estimate = cv2.ximgproc.guidedFilter(guide_image, depth_map, 8, 0.01)
    diff = depth_map - estimate
    diff = cv2.resize(diff, dsize=(diff.shape[1], diff.shape[0]), interpolation=cv2.INTER_CUBIC)
    depth_map = estimate + diff
    
    return depth_map