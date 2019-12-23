if [ "$#" -ne 1 ]; then
    echo "Usage: ./linear-bill.sh <bills>"
    echo "where <bills> is the number of times the sequence should be repeated."
    exit 0
fi

python3 src/repeatBill.py $1