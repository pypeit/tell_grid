cp ../make_tel_model.py .
python ../prepare_tell_runs.py Testing > test_runs.sh
sh test_runs.sh
python ../collate_grid.py Testing
rm make_tel_model.py


