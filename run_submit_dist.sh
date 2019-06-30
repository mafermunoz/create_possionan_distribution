for l in {1..100}
do
  for k in {1..3}
  do
    for i in {1..3}
      do
          sbatch submit_dist.sh  $l $k $i
        fi
      done
    done
  done
