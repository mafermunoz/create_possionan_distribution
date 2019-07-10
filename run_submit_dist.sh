for l in {1..100}
do
  for k in {1..3}
  do
    for i in {1..1}
      do
          OUTF='../pois_dist_year_new_'$i"_energy_bin"$k'_nmap_'$l'.npy'
          if [ ! -f ${OUTF} ]; then
            echo $l $k $i
            sbatch submit_dist.sh  $l $k $i
          fi
      done
    done
  done
