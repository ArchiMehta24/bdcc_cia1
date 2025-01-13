import cProfile
import merge_sort_serial
import merge_sort_multiprocessing

size = 50000
data = merge_sort_serial.generate_list(size)

print("Profiling Serial...")
cProfile.run('merge_sort_serial.merge_sort(data)')

print("Profiling Multiprocessing...")
cProfile.run('merge_sort_multiprocessing.merge_sort_parallel(data)')
