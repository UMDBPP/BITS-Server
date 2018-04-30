import multiprocessing

bind = "unix:/run/bits-server/bits.sock"
pidfile = "/run/bits-server/bits.pid"
accesslog = "/var/log/bits-server/access.log"
errorlog = "/var/log/bits-server/error.log"
workers = 2
