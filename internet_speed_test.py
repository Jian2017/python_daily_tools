# pip install speedtest-cli
import speedtest
import time

def get_download_upload_ping():
    servers = []
    # If you want to test against a specific server
    # servers = [1234]

    threads = None
    # If you want to use a single threaded test
    # threads = 1

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    results_dict = s.results.dict()
    
    return results_dict['download'], results_dict['upload'], results_dict['ping']


data = []
def foo():
    ti = time.ctime()
    try:
        da = get_download_upload_ping()
    except:
        da = (0,0,-1)
    
    print(ti,da)
    data.append([ [ti] + list(da)])

starttime=time.time()

while True:
    foo()
    time.sleep(300)
