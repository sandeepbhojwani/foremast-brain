from enum import Enum

#define all the constants
MAE = "mae"
DEVIATION = "deviation"

THRESHOLD = "threshold"
BOUND = "bound"
MIN_LOWER_BOUND = "min_lower_bound"

LOWER_BOUND = "lower_bound"
UPPER_BOUND = "upper_bound"
MIN_DATA_POINTS = "min_data_points"
LOWER_THRESHOLD = "lower_threshold"

DEFAULT_MIN_LOWER_BOUND = 0

LLOWER_BOUND = "llower_bound"
LUPPER_BOUND = "lupper_bound"

DEFAULT_THRESHOLD = 2
DEFAULT_LOWER_THRESHOLD =1.75

PAIRWISE_ALGORITHM = 'PAIRWISE_ALGORITHM'
PAIRWISE_THRESHOLD = 'PAIRWISE_THRESHOLD'

class REQUEST_STATE(Enum):
    COMPLETED_HEALTH = 'completed_health'
    COMPLETED_UNHEALTH = 'completed_unhealth'
    COMPLETED_UNKNOWN = 'completed_unknown'
    PREPROCESS_INPROGRESS = 'preprocess_inprogress'
    PREPROCESS_COMPLETED = 'preprocess_completed'
    PREPROCESS_FAILED = 'preprocess_failed'
    POSTPROCESS = 'postprocess_inprogress'
    INITIAL = 'initial'
    ABORT = 'abort'
    
class METRIC_PERIOD(Enum):
    CURRENT = 'current'
    HISTORICAL = 'historical'
    BASELINE = 'baseline'
    
class AI_MODEL(Enum):
    MOVING_AVERAGE_ALL = 'moving_average_all'
    MOVING_AVERAGE = 'moving_average'
    EXPONENTIAL_SMOOTHING = 'exponential_smoothing'
    DOUBLE_EXPONENTIAL_SMOOTHING = 'double_exponential_smoothing'
    HOLT_WINDER = 'holt_winder'
    PROPHET = 'prophet'
    BIVARIANT_GAUSSIAN = 'bivariant_gaussian'
    LSTM = 'lstm'
    


##Test ##   
#ll  = list(REQUEST_STATE)    
#print(len(ll))
#print(ll)
#dd =[c.value for c in REQUEST_STATE]
#print(dd)
#ww= REQUEST_STATE.COMPLETED_HEALTH
#print(type(REQUEST_STATE.COMPLETED_HEALTH.value))
#if (ww == REQUEST_STATE.COMPLETED_HEALTH):
#    print("True")
#else:
#    print("False")