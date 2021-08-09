import matplotlib.pyplot as plt
import numpy as np
import re
import argparse
import plistlib
import sys

def findDuplicates(fileName):
    
    print('Finding duplicates in %s....' % fileName)
    
    plist = plistlib.readPlist(fileName)
    
    tracks = plist['Tracks']
    
    trackNames = {}
    
    for trackID, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            
            if name in trackNames:
                
                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count+1)
                
            else:
                trackNames[name] = (duration, 1)
        
        except:
            pass
    
    duplicates = []
    
    for k,v in trackNames.items():
        if v[1] > 1:
            duplicates.append((v[1], k))
    
    if len(duplicates) > 0:
        print("Found %d duplicates. Tracknames saved to duplicates.txt" % len(dups))
    else:
        print("No duplicates found")
        
    f = open('duplicates.txt', 'w')
    for value in duplicates:
        f.write("[%d] %s\n" % (val[0], val[1]))
    f.close()

def findCommonTracks(filename):
    
    trackNamesets = []
    
    for filename in filenames:
        trackNames = set()
        
        plist = plistlib.readPlist(fileName)
        
        tracks = plist['Tracks']
        
        for trackID, track in tracks.items():
            try:
                trackNames.add(track['Name'])
            except:
                pass
        
    commonTracks = set.intersection(*trackNamesets)
    
    if len(commonTracks) > 0:
        f = open('commontracks.txt', 'w')
        for val in commonTracks:
            s = "%s\n" % val
            f.write(s.encode("UTF-8"))
        f.close()
        
        print("%d common tracks found. "
              "Track names written to common.txt." % len(commonTracks))
        
    else:
        print("No common tracks found")

def plotStats(fname):
    
    plist = plist.readPlist(fname)
    tracks = plist['Tracks']
    
    ratings = []
    durations = []
    
    for trackID, track in tracks.items():
        try:
            ratings.append(track['Album Rating'])
            durations.append(track['Total Time'])
            
        except:
            pass
    
    if ratings == [] or durations == []:
        print("No valid Album Rating/Total Time data in %s." % fileName)
        return
    
    x = np.array(durations, np.int32)
    
    x = x / 60000.0
    
    y = np.array(ratings, np.int32)
    
    plt.subplot(2, 1, 1)
    plt.plot(x,y,'o')
    
    plt.axis([0, 1.05*np.max(x), -1, 110])
    plt.xlabel('Track duration')
    plt.ylabel('Count')
    
    plt.show()

def main():
    
    parser = argparse.ArgumentParser(description=descStr)
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--common', nargs='*', dest='plFiles', required=False)
    group.add_argument('--stats', dest='plFile', required=False)
    group.add_argument('--dup', dest='plFileD', required=False)
    
    args = parser.parse_args()
    
    if args.plFiles:
        findCommonTracks(args.plFiles)
    elif args.plFile:
        plotStats(args.plFile)
    elif args.plFileD:
        findDuplicates(args.plFileD)
    
    else:
        print("These are not the tracks you are looking for")

if __name__ == '__main__':
    main()