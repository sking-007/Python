# import socket programming library
import socket

# import thread module
from _thread import *
import threading
import dataStructures
import time

print_lock = threading.Lock()

# thread function


def listToString(s):
    str = " "
    return (str.join(s))


def threaded(c):
    while True:
        message = 'What is the module id? ==>> '
        c.send(message.encode('ascii'))

        moduleId = c.recv(1024)
        moduleId = str(moduleId.decode('ascii'))

        message = '(L)earning Outcomes, (C)ourses, (A)ssessments or e(X)it? ==>> '
        c.send(message.encode('ascii'))

        choice = c.recv(1024)
        choice = str(choice.decode('ascii'))

        if (choice == 'L'):
            outcomes = dataStructures.learningOutcomes[moduleId]
            message = str(outcomes)
            c.send(message.encode('ascii'))

            change = c.recv(1024)
            change = str(change.decode('ascii'))
            print(change)

            if (change == 'A'):
                message = 'Enter new LO description ==>> '
                c.send(message.encode('ascii'))

                newLo = c.recv(1024)
                newLo = str(newLo.decode('ascii'))

                dataStructures.learningOutcomes[moduleId].append(newLo)

                outcomes = dataStructures.learningOutcomes[moduleId]
                message = str(outcomes)
                c.send(message.encode('ascii'))

            elif (change == 'D'):
                message = 'Enter LO # ==>> '
                c.send(message.encode('ascii'))

                newLo = c.recv(1024)
                newLo = str(newLo.decode('ascii'))

                dataStructures.learningOutcomes[moduleId].pop(int(newLo))

                outcomes = dataStructures.learningOutcomes[moduleId]
                message = str(outcomes)
                c.send(message.encode('ascii'))

            elif (change == 'E'):
                message = 'Enter LO # ==>> '
                c.send(message.encode('ascii'))

                newLoNum = c.recv(1024)
                newLoNum = str(newLoNum.decode('ascii'))

                message = 'Enter new LO # ==>> '
                c.send(message.encode('ascii'))

                newLo = c.recv(1024)
                newLo = str(newLo.decode('ascii'))

                dataStructures.learningOutcomes[moduleId][int(
                    newLoNum)] = newLo

                outcomes = dataStructures.learningOutcomes[moduleId]
                message = str(outcomes)
                c.send(message.encode('ascii'))

            elif (change == 'E'):
                pass

        elif (choice == 'C'):
            message = dataStructures.course
            c.send(message.encode('ascii'))
            time.sleep(1)

        elif (choice == 'A'):
            outcomes = dataStructures.assessments
            message = str(outcomes)
            c.send(message.encode('ascii'))
            time.sleep(1)


        elif (choice == 'X'):
            break
        else:
            print('Invalid Input')

    print('Bye')

    # lock released on exit
    print_lock.release()
    c.close()

    # # reverse the given string from client
    # data = data[::-1]

    # # send back reversed string to client
    # c.send(data)

    # connection closed


def Main():
    host = ""

    # reserve a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()
