import AbstractApplication as Base
from threading import Semaphore
import random
from timeit import default_timer as timer
import time
import os


class DialogFlowSampleApplication(Base.AbstractApplication):
    def main(self):
        # Set the correct language (and wait for it to be changed)
        self.langLock = Semaphore(0)
        self.setLanguage('en-US')
        self.langLock.acquire()

        # Pass the required Dialogflow parameters (add your Dialogflow parameters)
        self.setDialogflowKey('nursebot-gmgphj-31fa6ff7d87f.json')
        self.setDialogflowAgent('nursebot-gmgphj')

        self.gestureLock = Semaphore(0)
        self.doGesture("animations/Stand/Gestures/Hey_1")

        self.name = None
        self.speechLock = Semaphore(0)
        self.sayAnimated('Hello,my name is kobe,I am your personal nurse robot, I am going to take good care of your health. So, let me know you first.whats your name？')
        self.speechLock.acquire()
        self.gestureLock.acquire()

        # Listen for an answer for at most 5 seconds
        # Doing wave at same time when saying 'hello'

        # Keep listening patient's name if the robot doesn't recognize the answer
        while not self.name:
            self.nameLock = Semaphore(0)
            self.setAudioContext('answer_name')

            self.startListening()
            self.nameLock.acquire(timeout=5)
            self.stopListening()
            print(self.name)

            if self.name:
                self.sayAnimated('Nice to meet you ' + self.name + '!'+'I am going to record your heartrate and then your breakfast preference')
                print(self.name)
            else:
                self.sayAnimated('Sorry, I didn\'t catch your name.'+'could you repeat it again?')

            self.speechLock.acquire()

        # Measuring heartrate through choregraphe
        self.gestureLock = Semaphore(0)
        self.doGesture("heartrate-0a71b6/behavior_1")
        self.gestureLock.acquire()

        # Make the robot ask the question, and wait until it is done speaking
        time.sleep(2)
        self.answer_breakfast = None
        number = 0
        self.speechLock = Semaphore(0)
        self.sayAnimated('what would you like in breakfast？bread or toast?')
        self.speechLock.acquire()

        # Listen for an answer for at most 5 seconds
        # Keep listening patient's answer if the robot doesn't recognize it 2 times
        while not self.answer_breakfast and number < 2:
            self.nameLock = Semaphore(0)
            self.setAudioContext('answer_breakfast')
            self.startListening()
            self.nameLock.acquire(timeout=5)
            self.stopListening()

            if not self.answer_breakfast:  # wait one more second after stopListening (if needed)
                self.nameLock.acquire(timeout=1)

            # Respond and wait for that to finish

            if self.answer_breakfast:
                self.sayAnimated('Nice choice ' +self.answer_breakfast+'is good for your health'+'!')
                break
            elif number == 1:
                self.sayAnimated('Sorry, I didn\'t catch your answer'+'You can answer this question by touching my arm')
                self.gestureLock = Semaphore(0)
                self.doGesture("heartrate-0a71b6/TouchBreadToast")
                self.gestureLock.acquire()
                break

            # If the robot doesn't recognize patient's answer 2 times, then doing choregraphe to recognize answer by touching the senor on robot's arm

            else:
                self.sayAnimated('Sorry, I didn\'t catch your answer.'+'can you say it again?')

            self.speechLock.acquire()
            number += 1

        # Make the robot ask the question, and wait until it is done speaking
        time.sleep(2)
        self.answer_drink = None
        num = 0
        self.speechLock = Semaphore(0)
        self.sayAnimated('what would you like to drink？coffee or tea? or would like cola to make you so cool?')
        self.speechLock.acquire()

        # Listen for an answer for at most 5 seconds
        # Keep listening patient's answer if the robot doesn't recognize it 2 times
        while not self.answer_drink and num < 2:
            self.nameLock = Semaphore(0)
            self.setAudioContext('answer_drinks')
            time.sleep(5)
            self.startListening()
            self.nameLock.acquire(timeout=5)
            self.stopListening()

            if not self.answer_drink:  # wait one more second after stopListening (if needed)
                self.nameLock.acquire(timeout=1)

            # Respond and wait for that to finish

            if self.answer_drink:
                self.sayAnimated('Cool, you can do anything with ' + self.answer_drink + '!')
                break
            elif num == 1:
                self.sayAnimated('Sorry, I didn\'t catch your answer'+'you can answer this question by touching my arm')
                self.gestureLock = Semaphore(0)
                self.doGesture("heartrate-0a71b6/Touch")
                self.gestureLock.acquire()
                break

            # If the robot doesn't recognize patient's answer 2 times, then doing choregraphe to recognize answer by touching the senor on robot's arm

            else:
                self.sayAnimated('Sorry, I didn\'t catch your answer.'+'could you repeat?')

            self.speechLock.acquire()
            num += 1


        time.sleep(2)
        self.answer_topping = None
        count = 0
        self.speechLock = Semaphore(0)
        self.sayAnimated('what else would you like for breakfast ? ham or cheese?')
        self.speechLock.acquire()

        # Listen for an answer for at most 5 seconds
        # Keep listening patient's answer if the robot doesn't recognize it 2 times
        while not self.answer_topping and count < 2:
            self.nameLock = Semaphore(0)
            self.setAudioContext('answer_topping')
            time.sleep(3)
            self.startListening()
            self.nameLock.acquire(timeout=5)
            self.stopListening()

            if not self.answer_topping:  # wait one more second after stopListening (if needed)
                self.nameLock.acquire(timeout=1)

            # Respond and wait for that to finish

            if self.answer_topping:
                self.sayAnimated(self.answer_topping+'is Perfect '+'I will send your preference to nurse'+'You can enjoy it in 30 minutes'+'Have a nice day!')
            elif count == 1:
                self.sayAnimated('Sorry, I didn\'t catch your answer'+'You can answer this question by touching my arm')
                self.gestureLock = Semaphore(0)
                self.doGesture("heartrate-0a71b6/TouchCheeseHam")
                self.gestureLock.acquire()
                time.sleep(2)
                self.sayAnimated('I will send your preference to the nurse'+'you can enjoy it in 30 minutes'+'Have a nice day'+'!')

                # If the robot doesn't recognize patient's answer 2 times, then doing choregraphe to recognize answer by touching the senor on robot's arm

            else:
                self.sayAnimated('Sorry, I didn\'t catch your answer.'+'could you please say it again?')

            self.speechLock.acquire()
            count += 1

        # Display a gesture (replace <gestureID> with your gestureID)
        self.gestureLock = Semaphore(0)
        self.doGesture('<gestureID>/behavior_1')
        self.gestureLock.acquire()

    def onRobotEvent(self, event):
        if event == 'LanguageChanged':
            self.langLock.release()
        elif event == 'TextDone':
            self.speechLock.release()
        elif event == 'GestureDone':
            self.gestureLock.release()

    def onAudioIntent(self, *args, intentName):
        if intentName == 'answer_breakfast' and len(args) > 0:
            self.answer_breakfast = args[0]
            self.nameLock.release()
        elif intentName == 'answer_name' and len(args) > 0:
            self.name = args[0]
            self.nameLock.release()
        elif intentName == 'answer_drinks' and len(args) > 0:
            self.answer_drink = args[0]
            self.nameLock.release()
        elif intentName == 'answer_topping' and len(args) > 0:
            self.answer_topping = args[0]
            self.nameLock.release()


# Run the application
sample = DialogFlowSampleApplication()
sample.main()
sample.stop()