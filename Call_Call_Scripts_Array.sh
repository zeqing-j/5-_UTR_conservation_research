#!/bin/bash

#!/bin/bash

# Base index for starting point
BASE=0
MAX_INDEX=999
# Ending point for the current chunk


# Total number of tasks (subtract 1 because we're starting at 0)
TOTAL_TASKS=38590

while [ $BASE -le $TOTAL_TASKS ]; do
    # If END exceeds TOTAL_TASKS, set END to TOTAL_TASKS
    END=$((BASE+MAX_INDEX))
    if [ $END -gt $TOTAL_TASKS ]; then
        END=$TOTAL_TASKS
    fi
    
    # Submit the job array for the current range
    sbatch --array=$BASE-$END /ocean/projects/bio200049p/smishra1/Scripts/Parallel/Call_Scripts_Array.sh

    # Move to the next range
    BASE=$((END+1))
    echo $BASE
    #END=$((END+1000))
done

