import random, time

Bar = chr(9608)


def progressbar(progress, Total, barWidth=40):

    progressBar = ''
    progressBar += '['

    if progress > Total:
        progress = Total
    if progress < 0:
        progress = 0

    numberofBars = int((progress/Total)*barWidth)
    progressBar += Bar * numberofBars 
    progressBar += ' ' * (barWidth - numberofBars)
    progressBar += ']'

    percentComplete = round(progress / Total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'

    progressBar += ' ' + str(progress) + '/' + str(Total)

    return progressBar


print("Progress Bar")
bytesDownloaded = 0
byteSize = 4096

while byteSize > bytesDownloaded:

    bytesDownloaded += random.randint(0, 100)

    barStr = progressbar(bytesDownloaded, byteSize)

    print(barStr, end= '', flush=True)

    time.sleep(0.2)

    print('\b' * len(barStr), end='', flush=True)

