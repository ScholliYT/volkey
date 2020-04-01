from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import argparse

def changeVolumeOfApplication(application_name, amount):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process:
            if session.Process.name() == application_name:
                changeVolume(volume, amount)
                print("%s: %s" % (application_name, round(volume.GetMasterVolume()*100)))

def changeVolume(volume, amount):
    newvolume = volume.GetMasterVolume() + amount
    if newvolume > 1.0:
        newvolume = 1.0
    elif newvolume < 0:
        newvolume = 0
    volume.SetMasterVolume(newvolume, None)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('amount', help="amount to change the value by from -100 to 100 i.e. -2.5") 
    parser.add_argument('-a', '--application', required=False, help="the name of the application to change volume of")
    args = parser.parse_args()

    if args.application:
        changeVolumeOfApplication(args.application, float(args.amount)/100)
    else:
        print("not yet implemented!")