import multiprocessing
import subprocess

NUM_INSTANCES = 10

def run_instance(instance_id):
    # Replace with the command to run your script
    subprocess.run(['python', 'src/ds_runner.py', str(instance_id)])

def spawn_instances():
    processes = []

    for i in range(NUM_INSTANCES):
        p = multiprocessing.Process(target=run_instance, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

def main():
    spawn_instances()

if __name__ == "__main__":
    main()