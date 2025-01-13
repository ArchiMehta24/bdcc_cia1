Profiling Serial...
         2627032 function calls (2527034 primitive calls) in 0.415 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.415    0.415 <string>:1(<module>)
    49999    0.271    0.000    0.364    0.000 merge_sort_serial.py:15(merge)
  99999/1    0.045    0.000    0.415    0.415 merge_sort_serial.py:7(merge_sort)
        1    0.000    0.000    0.415    0.415 {built-in method builtins.exec}
  1658846    0.064    0.000    0.064    0.000 {built-in method builtins.len}
   718187    0.030    0.000    0.030    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    99998    0.006    0.000    0.006    0.000 {method 'extend' of 'list' objects}


Profiling Multiprocessing...
         155688 function calls (155561 primitive calls) in 0.241 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:100(acquire)
     27/4    0.000    0.000    0.006    0.002 <frozen importlib._bootstrap>:1022(_find_and_load)
    12/11    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:1053(_handle_fromlist)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:125(release)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:165(__init__)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:169(__enter__)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:173(__exit__)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:179(_get_module_lock)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:198(cb)
     35/4    0.000    0.000    0.005    0.001 <frozen importlib._bootstrap>:233(_call_with_frames_removed)
      283    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:244(_verbose_message)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:254(_requires_builtin_wrapper)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:357(__init__)
       36    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:391(cached)
       51    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:404(parent)
       25    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:412(has_location)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:421(spec_from_loader)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:48(_new_module)
       25    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:492(_init_module_attrs)
       25    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:564(module_from_spec)
     25/4    0.000    0.000    0.006    0.001 <frozen importlib._bootstrap>:664(_load_unlocked)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:71(__init__)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:746(find_spec)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:770(create_module)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:778(exec_module)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:795(is_package)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:826(find_spec)
       71    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:893(__enter__)
       71    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:897(__exit__)
       27    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:921(_find_spec)
     27/4    0.000    0.000    0.006    0.001 <frozen importlib._bootstrap>:987(_find_and_load_unlocked)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1040(__init__)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1065(get_filename)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1070(get_data)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1089(path_stats)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1163(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1174(create_module)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1182(exec_module)
      250    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:126(_path_join)
      250    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:128(<listcomp>)
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:132(_path_split)
       64    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:134(<genexpr>)
       66    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1356(_path_importer_cache)
       22    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1399(_get_spec)
       86    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:140(_path_stat)
       22    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1431(find_spec)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:150(_path_is_mode_type)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1531(_get_spec)
       50    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1536(find_spec)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:159(_path_isfile)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:180(_path_isabs)
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:380(cache_from_source)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:510(_get_cached)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:542(_check_name_wrapper)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:585(_classify_pyc)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:618(_validate_timestamp_pyc)
       16    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:670(_compile_bytecode)
       50    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:71(_relax_case)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:721(spec_from_file_location)
       48    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_unpack_uint32)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:874(create_module)
     16/4    0.000    0.000    0.006    0.001 <frozen importlib._bootstrap_external>:877(exec_module)
       16    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:950(get_code)
        1    0.000    0.000    0.241    0.241 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:328(namedtuple)
        4    0.000    0.000    0.000    0.000 __init__.py:402(<genexpr>)
        1    0.000    0.000    0.000    0.000 _compression.py:1(<module>)
        1    0.000    0.000    0.000    0.000 _compression.py:33(DecompressReader)
        1    0.000    0.000    0.000    0.000 _compression.py:9(BaseStream)
        5    0.000    0.000    0.000    0.000 _weakrefset.py:39(_remove)
        5    0.000    0.000    0.000    0.000 _weakrefset.py:86(add)
        4    0.000    0.000    0.000    0.000 abc.py:105(__new__)
        1    0.000    0.000    0.000    0.000 bz2.py:1(<module>)
        1    0.000    0.000    0.000    0.000 bz2.py:26(BZ2File)
        1    0.000    0.000    0.003    0.003 connection.py:1(<module>)
        1    0.000    0.000    0.000    0.000 connection.py:114(_ConnectionBase)
        6    0.000    0.000    0.000    0.000 connection.py:117(__init__)
        6    0.000    0.000    0.000    0.000 connection.py:130(__del__)
        3    0.000    0.000    0.000    0.000 connection.py:134(_check_closed)
        3    0.000    0.000    0.000    0.000 connection.py:142(_check_writable)
        3    0.000    0.000    0.000    0.000 connection.py:181(send_bytes)
        1    0.000    0.000    0.000    0.000 connection.py:348(Connection)
        6    0.000    0.000    0.000    0.000 connection.py:360(_close)
        3    0.000    0.000    0.000    0.000 connection.py:365(_send)
        3    0.000    0.000    0.000    0.000 connection.py:390(_send_bytes)
        1    0.000    0.000    0.000    0.000 connection.py:432(Listener)
        3    0.000    0.000    0.000    0.000 connection.py:516(Pipe)
        1    0.000    0.000    0.000    0.000 connection.py:579(SocketListener)
        1    0.000    0.000    0.000    0.000 connection.py:765(ConnectionWrapper)
        1    0.000    0.000    0.000    0.000 connection.py:787(XmlListener)
        3    0.000    0.000    0.001    0.000 context.py:110(SimpleQueue)
        1    0.000    0.000    0.009    0.009 context.py:115(Pool)
        9    0.000    0.000    0.000    0.000 context.py:187(get_context)
        6    0.000    0.000    0.000    0.000 context.py:197(get_start_method)
        1    0.000    0.000    0.000    0.000 context.py:237(get_context)
        2    0.000    0.000    0.002    0.001 context.py:278(_Popen)
        6    0.000    0.000    0.001    0.000 context.py:65(Lock)
        1    0.000    0.000    0.000    0.000 fnmatch.py:1(<module>)
        1    0.000    0.000    0.000    0.000 functools.py:35(update_wrapper)
        1    0.000    0.000    0.000    0.000 functools.py:479(lru_cache)
        1    0.000    0.000    0.000    0.000 functools.py:518(decorating_function)
        1    0.000    0.000    0.000    0.000 heapq.py:1(<module>)
        1    0.000    0.000    0.000    0.000 lzma.py:1(<module>)
        1    0.000    0.000    0.000    0.000 lzma.py:38(LZMAFile)
        1    0.001    0.001    0.241    0.241 merge_sort_multiprocessing.py:30(merge_sort_parallel)
        1    0.019    0.019    0.025    0.025 merge_sort_multiprocessing.py:8(merge)
        1    0.000    0.000    0.005    0.005 pool.py:1(<module>)
        1    0.000    0.000    0.000    0.000 pool.py:150(_PoolCache)
        1    0.000    0.000    0.000    0.000 pool.py:157(__init__)
        1    0.000    0.000    0.000    0.000 pool.py:173(Pool)
        2    0.000    0.000    0.000    0.000 pool.py:179(Process)
        1    0.000    0.000    0.004    0.004 pool.py:183(__init__)
        1    0.000    0.000    0.000    0.000 pool.py:266(__del__)
        1    0.000    0.000    0.000    0.000 pool.py:279(_get_sentinels)
        1    0.000    0.000    0.002    0.002 pool.py:305(_repopulate_pool)
        1    0.000    0.000    0.002    0.002 pool.py:314(_repopulate_pool_static)
        1    0.000    0.000    0.001    0.001 pool.py:345(_setup_queues)
        2    0.000    0.000    0.000    0.000 pool.py:351(_check_running)
        1    0.000    0.000    0.205    0.205 pool.py:362(map)
        1    0.000    0.000    0.000    0.000 pool.py:471(_map_async)
        1    0.000    0.000    0.000    0.000 pool.py:57(RemoteTraceback)
        1    0.000    0.000    0.000    0.000 pool.py:63(ExceptionWithTraceback)
        1    0.000    0.000    0.001    0.001 pool.py:654(terminate)
        1    0.000    0.000    0.000    0.000 pool.py:671(_help_stuff_finish)
        1    0.000    0.000    0.001    0.001 pool.py:680(_terminate_pool)
        1    0.000    0.000    0.000    0.000 pool.py:734(__enter__)
        1    0.000    0.000    0.001    0.001 pool.py:738(__exit__)
        1    0.000    0.000    0.000    0.000 pool.py:745(ApplyResult)
        1    0.000    0.000    0.000    0.000 pool.py:747(__init__)
        1    0.000    0.000    0.000    0.000 pool.py:756(ready)
        1    0.000    0.000    0.204    0.204 pool.py:764(wait)
        1    0.000    0.000    0.205    0.205 pool.py:767(get)
        1    0.000    0.000    0.000    0.000 pool.py:794(MapResult)
        1    0.000    0.000    0.000    0.000 pool.py:796(__init__)
        1    0.000    0.000    0.000    0.000 pool.py:80(MaybeEncodingError)
        1    0.000    0.000    0.000    0.000 pool.py:837(IMapIterator)
        1    0.000    0.000    0.000    0.000 pool.py:906(IMapUnorderedIterator)
        1    0.000    0.000    0.000    0.000 pool.py:921(ThreadPool)
        1    0.000    0.000    0.000    0.000 popen_fork.py:1(<module>)
        1    0.000    0.000    0.000    0.000 popen_fork.py:12(Popen)
        2    0.000    0.000    0.001    0.001 popen_fork.py:15(__init__)
        6    0.000    0.000    0.001    0.000 popen_fork.py:24(poll)
        1    0.000    0.000    0.001    0.001 popen_fork.py:36(wait)
        2    0.000    0.000    0.000    0.000 popen_fork.py:46(_send_signal)
        2    0.000    0.000    0.000    0.000 popen_fork.py:56(terminate)
        2    0.000    0.000    0.001    0.001 popen_fork.py:62(_launch)
        2    0.000    0.000    0.002    0.001 process.py:110(start)
        2    0.000    0.000    0.000    0.000 process.py:128(terminate)
        1    0.000    0.000    0.001    0.001 process.py:142(join)
        2    0.000    0.000    0.000    0.000 process.py:153(is_alive)
        4    0.000    0.000    0.000    0.000 process.py:189(name)
        2    0.000    0.000    0.000    0.000 process.py:193(name)
        2    0.000    0.000    0.000    0.000 process.py:205(daemon)
        2    0.000    0.000    0.000    0.000 process.py:224(exitcode)
        1    0.000    0.000    0.000    0.000 process.py:234(ident)
        6    0.000    0.000    0.000    0.000 process.py:37(current_process)
        2    0.000    0.000    0.000    0.000 process.py:61(_cleanup)
        2    0.000    0.000    0.000    0.000 process.py:80(__init__)
        4    0.000    0.000    0.000    0.000 process.py:94(<genexpr>)
       10    0.000    0.000    0.000    0.000 process.py:99(_check_closed)
        1    0.000    0.000    0.000    0.000 queue.py:1(<module>)
        1    0.000    0.000    0.000    0.000 queue.py:223(PriorityQueue)
        1    0.000    0.000    0.000    0.000 queue.py:23(Full)
        1    0.000    0.000    0.000    0.000 queue.py:242(LifoQueue)
        1    0.000    0.000    0.000    0.000 queue.py:258(_PySimpleQueue)
        1    0.000    0.000    0.000    0.000 queue.py:28(Queue)
        1    0.000    0.000    0.000    0.000 queues.py:1(<module>)
        1    0.000    0.000    0.000    0.000 queues.py:294(JoinableQueue)
        1    0.000    0.000    0.000    0.000 queues.py:337(SimpleQueue)
        3    0.000    0.000    0.001    0.000 queues.py:339(__init__)
        1    0.000    0.000    0.000    0.000 queues.py:35(Queue)
        3    0.000    0.000    0.000    0.000 queues.py:369(put)
        1    0.000    0.000    0.000    0.000 random.py:119(__init__)
        1    0.000    0.000    0.000    0.000 random.py:128(seed)
        6    0.000    0.000    0.000    0.000 random.py:506(choices)
        6    0.000    0.000    0.000    0.000 random.py:519(<listcomp>)
        3    0.000    0.000    0.000    0.000 reduction.py:38(__init__)
        1    0.000    0.000    0.000    0.000 reduction.py:43(register)
        3    0.000    0.000    0.000    0.000 reduction.py:48(dumps)
        1    0.000    0.000    0.002    0.002 shutil.py:1(<module>)
        1    0.000    0.000    0.000    0.000 shutil.py:59(Error)
        1    0.000    0.000    0.000    0.000 shutil.py:62(SameFileError)
        1    0.000    0.000    0.000    0.000 shutil.py:65(SpecialFileError)
        1    0.000    0.000    0.000    0.000 shutil.py:69(ExecError)
        1    0.000    0.000    0.000    0.000 shutil.py:72(ReadError)
        1    0.000    0.000    0.000    0.000 shutil.py:75(RegistryError)
        1    0.000    0.000    0.000    0.000 shutil.py:79(_GiveupOnFastCopy)
        1    0.000    0.000    0.000    0.000 subprocess.py:1(<module>)
        1    0.000    0.000    0.000    0.000 subprocess.py:101(SubprocessError)
        1    0.000    0.000    0.000    0.000 subprocess.py:104(CalledProcessError)
        1    0.000    0.000    0.000    0.000 subprocess.py:141(TimeoutExpired)
        1    0.000    0.000    0.000    0.000 subprocess.py:425(CompletedProcess)
        1    0.000    0.000    0.000    0.000 subprocess.py:648(_use_posix_spawn)
        1    0.000    0.000    0.000    0.000 subprocess.py:702(Popen)
        1    0.000    0.000    0.000    0.000 synchronize.py:1(<module>)
        6    0.000    0.000    0.000    0.000 synchronize.py:114(_make_name)
        1    0.000    0.000    0.000    0.000 synchronize.py:123(Semaphore)
        1    0.000    0.000    0.000    0.000 synchronize.py:142(BoundedSemaphore)
        1    0.000    0.000    0.000    0.000 synchronize.py:159(Lock)
        6    0.000    0.000    0.000    0.000 synchronize.py:161(__init__)
        1    0.000    0.000    0.000    0.000 synchronize.py:184(RLock)
        1    0.000    0.000    0.000    0.000 synchronize.py:210(Condition)
        1    0.000    0.000    0.000    0.000 synchronize.py:321(Event)
        1    0.000    0.000    0.000    0.000 synchronize.py:360(Barrier)
        1    0.000    0.000    0.000    0.000 synchronize.py:46(SemLock)
        6    0.000    0.000    0.000    0.000 synchronize.py:50(__init__)
        6    0.000    0.000    0.000    0.000 synchronize.py:90(_make_methods)
        3    0.000    0.000    0.000    0.000 synchronize.py:94(__enter__)
        3    0.000    0.000    0.000    0.000 synchronize.py:97(__exit__)
        1    0.000    0.000    0.002    0.002 tempfile.py:1(<module>)
        1    0.000    0.000    0.000    0.000 tempfile.py:271(_RandomNameSequence)
        6    0.000    0.000    0.000    0.000 tempfile.py:281(rng)
        6    0.000    0.000    0.000    0.000 tempfile.py:292(__next__)
        1    0.000    0.000    0.000    0.000 tempfile.py:571(_TemporaryFileCloser)
        1    0.000    0.000    0.000    0.000 tempfile.py:614(_TemporaryFileWrapper)
        1    0.000    0.000    0.000    0.000 tempfile.py:816(SpooledTemporaryFile)
        1    0.000    0.000    0.000    0.000 tempfile.py:960(TemporaryDirectory)
        3    0.000    0.000    0.000    0.000 threading.py:1028(_stop)
        3    0.000    0.000    0.000    0.000 threading.py:1064(join)
        5    0.000    0.000    0.000    0.000 threading.py:1102(_wait_for_tstate_lock)
        2    0.000    0.000    0.000    0.000 threading.py:1169(is_alive)
        6    0.000    0.000    0.000    0.000 threading.py:1183(daemon)
        3    0.000    0.000    0.000    0.000 threading.py:1198(daemon)
        3    0.000    0.000    0.000    0.000 threading.py:1301(_make_invoke_excepthook)
        9    0.000    0.000    0.000    0.000 threading.py:1430(current_thread)
        4    0.000    0.000    0.000    0.000 threading.py:236(__init__)
        4    0.000    0.000    0.000    0.000 threading.py:264(__enter__)
        4    0.000    0.000    0.000    0.000 threading.py:267(__exit__)
        4    0.000    0.000    0.000    0.000 threading.py:273(_release_save)
        4    0.000    0.000    0.000    0.000 threading.py:276(_acquire_restore)
        4    0.000    0.000    0.000    0.000 threading.py:279(_is_owned)
        4    0.000    0.000    0.205    0.051 threading.py:288(wait)
        4    0.000    0.000    0.000    0.000 threading.py:545(__init__)
       12    0.000    0.000    0.000    0.000 threading.py:553(is_set)
        4    0.000    0.000    0.205    0.051 threading.py:589(wait)
        3    0.000    0.000    0.000    0.000 threading.py:782(_newname)
        3    0.000    0.000    0.000    0.000 threading.py:827(__init__)
        3    0.000    0.000    0.001    0.000 threading.py:916(start)
        1    0.000    0.000    0.000    0.000 traceback.py:1(<module>)
        1    0.000    0.000    0.000    0.000 traceback.py:243(FrameSummary)
        1    0.000    0.000    0.000    0.000 traceback.py:335(StackSummary)
        1    0.000    0.000    0.000    0.000 traceback.py:457(TracebackException)
        1    0.000    0.000    0.000    0.000 traceback.py:87(_Sentinel)
        1    0.000    0.000    0.001    0.001 util.py:1(<module>)
        1    0.000    0.000    0.000    0.000 util.py:108(_platform_supports_abstract_sockets)
        6    0.000    0.000    0.000    0.000 util.py:171(register_after_fork)
        1    0.000    0.000    0.000    0.000 util.py:182(Finalize)
        3    0.000    0.000    0.000    0.000 util.py:186(__init__)
        3    0.000    0.000    0.001    0.000 util.py:205(__call__)
        1    0.000    0.000    0.000    0.000 util.py:368(ForkAwareThreadLock)
        1    0.000    0.000    0.000    0.000 util.py:385(ForkAwareLocal)
        2    0.000    0.000    0.000    0.000 util.py:433(_flush_std_streams)
        3    0.000    0.000    0.000    0.000 util.py:44(sub_debug)
        2    0.000    0.000    0.000    0.000 util.py:461(close_fds)
       18    0.000    0.000    0.000    0.000 util.py:48(debug)
        1    0.000    0.000    0.000    0.000 weakref.py:105(__init__)
        6    0.000    0.000    0.000    0.000 weakref.py:106(remove)
        6    0.000    0.000    0.000    0.000 weakref.py:165(__setitem__)
        1    0.000    0.000    0.000    0.000 weakref.py:290(update)
        6    0.000    0.000    0.000    0.000 weakref.py:348(__new__)
        6    0.000    0.000    0.000    0.000 weakref.py:353(__init__)
       10    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x65532d0449a0}
        4    0.000    0.000    0.000    0.000 {built-in method _abc._abc_init}
       16    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
      125    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        5    0.000    0.000    0.000    0.000 {built-in method _imp.create_builtin}
        4    0.000    0.000    0.000    0.000 {built-in method _imp.create_dynamic}
        5    0.000    0.000    0.000    0.000 {built-in method _imp.exec_builtin}
        4    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
       21    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
       22    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
      125    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        3    0.000    0.000    0.000    0.000 {built-in method _struct.pack}
       63    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
       63    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        3    0.000    0.000    0.000    0.000 {built-in method _thread.start_new_thread}
        6    0.000    0.000    0.000    0.000 {built-in method _weakref._remove_dead_weakref}
        1    0.000    0.000    0.000    0.000 {built-in method atexit.register}
       61    0.001    0.000    0.001    0.000 {built-in method builtins.__build_class__}
        1    0.000    0.000    0.001    0.001 {built-in method builtins.__import__}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.divmod}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.eval}
     17/1    0.000    0.000    0.241    0.241 {built-in method builtins.exec}
      154    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
      141    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.id}
      119    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
   100090    0.005    0.000    0.005    0.000 {built-in method builtins.len}
       32    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       18    0.000    0.000    0.000    0.000 {built-in method builtins.next}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
       48    0.000    0.000    0.000    0.000 {built-in method from_bytes}
       16    0.000    0.000    0.000    0.000 {built-in method io.open_code}
       16    0.001    0.000    0.001    0.000 {built-in method marshal.loads}
       48    0.000    0.000    0.000    0.000 {built-in method math.floor}
       14    0.000    0.000    0.000    0.000 {built-in method posix.close}
        1    0.000    0.000    0.000    0.000 {built-in method posix.confstr}
        2    0.001    0.000    0.001    0.000 {built-in method posix.fork}
       52    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
       19    0.000    0.000    0.000    0.000 {built-in method posix.getpid}
        2    0.000    0.000    0.000    0.000 {built-in method posix.kill}
        7    0.000    0.000    0.000    0.000 {built-in method posix.pipe}
       86    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        1    0.000    0.000    0.000    0.000 {built-in method posix.sysconf}
        6    0.001    0.000    0.001    0.000 {built-in method posix.waitpid}
        2    0.000    0.000    0.000    0.000 {built-in method posix.waitstatus_to_exitcode}
        3    0.000    0.000    0.000    0.000 {built-in method posix.write}
        1    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        4    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 {function Random.seed at 0x7e5c90e9dc60}
        4    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        3    0.000    0.000    0.000    0.000 {method '__enter__' of '_multiprocessing.SemLock' objects}
        4    0.000    0.000    0.000    0.000 {method '__enter__' of '_thread.lock' objects}
       16    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        3    0.000    0.000    0.000    0.000 {method '__exit__' of '_multiprocessing.SemLock' objects}
        3    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.RLock' objects}
       58    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
        1    0.000    0.000    0.000    0.000 {method 'acquire' of '_multiprocessing.SemLock' objects}
       19    0.205    0.011    0.205    0.011 {method 'acquire' of '_thread.lock' objects}
       10    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        4    0.000    0.000    0.000    0.000 {method 'append' of 'collections.deque' objects}
    50002    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        5    0.000    0.000    0.000    0.000 {method 'copy' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        7    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        3    0.000    0.000    0.000    0.000 {method 'dump' of '_pickle.Pickler' objects}
       24    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        4    0.000    0.000    0.000    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        3    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
       57    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 {method 'getbuffer' of '_io.BytesIO' objects}
        4    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
      292    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {method 'locked' of '_thread.lock' objects}
       25    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'put' of '_queue.SimpleQueue' objects}
       48    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
       16    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
        7    0.000    0.000    0.000    0.000 {method 'release' of '_thread.lock' objects}
        3    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       32    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
      166    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
      532    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        5    0.000    0.000    0.000    0.000 {method 'setter' of 'property' objects}
        3    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       24    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}

