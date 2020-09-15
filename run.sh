#run.sh
echo "Enter x:"
read x
echo "Enter y:"
read y
r=`python ./library.py --a $x --b $y`
echo "$x+$y=$r"
