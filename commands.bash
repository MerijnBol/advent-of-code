new() {(
    year=$1
    day=$2

    echo "Creating directory..."
    dir=$(mkdir $year/$day)

    echo "Copying default files..."
    # Copy contents of the 'new_day' folder, but never overwrite anything.
    cp -rn ./new_day/* ./$year/$day
    echo "done"
);}

run() {(
    year=$1
    day=$2
    flag=$3

    python $year/$day/puzzle.py $3
);}
