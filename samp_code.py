import boto3
from codeguru_profiler_agent import Profiler

alph = "abcdefghijklmnopqrstuvwxyz"

print(alph[3:15])
print(alph[3:15:3])
print(alph[15:3:-3])
print(alph[::-3])

conn_string = "ghost"
pwd = "khk"
keys = "khaki"


def start_application():
    pass


if __name__ == "__main__":
    custom_session = boto3.session.Session(profile_name='dev', region_name='us-east-1')
    Profiler(profiling_group_name="pyprofiler", aws_session=custom_session).start()
    start_application()
