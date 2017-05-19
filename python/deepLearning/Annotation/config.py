# path and dataset parameter
#

#CLASSES = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus',
#           'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse',
#           'motorbike', 'person', 'pottedplant', 'sheep', 'sofa',
#           'train', 'tvmonitor']

#CLASSES = ['钳子', '克丝钳', '尖嘴钳', '扭力扳手', '活口扳手', '十字改锥', '一字改锥', '大锤', '大扳']
#CLASSES_EN = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


CLASSES = ['钳子', '克丝钳', '尖嘴钳', '扭力扳手', '活口扳手', '十字改锥', '一字改锥', '大锤', '大扳','扳手','活口扳手12寸','梅花扳手','大镊子','量尺','塞尺','双截棍','拐弯内五角','铁片']
CLASSES_EN = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','aa','ab','ac','ad','ae','af','ag','ah','ai']
CLASSES_NUM = len(CLASSES)
LABELS_EN2CN = dict(zip(CLASSES_EN, CLASSES))
LABELS_CN2EN = dict(zip(CLASSES, CLASSES_EN))

FLIPPED = True

#ignore_missing_scope = 'yolo/fc_36'
ignore_missing_scope = None

#
# model parameter
#

IMAGE_SIZE_YOLO = 448
IMAGE_SIZE = 299
IMAGE_CHANNEL = 3

CELL_SIZE = 7
BOXES_PER_CELL = 2

ALPHA = 0.1

DISP_CONSOLE = False

OBJECT_SCALE = 1.0
NOOBJECT_SCALE = 1.0
CLASS_SCALE = 2.0
COORD_SCALE = 5.0


#
# solver parameter
#

GPU = ''

LEARNING_RATE = 0.0001

DECAY_STEPS = 10000

DECAY_RATE = 0.1

STAIRCASE = True

BATCH_SIZE = 8

MAX_ITER = 9000000

SUMMARY_ITER = 1

EVAL_ITER = 100

SAVE_ITER = 1000


#
# test parameter
#

THRESHOLD = 0.2

IOU_THRESHOLD = 0.5
