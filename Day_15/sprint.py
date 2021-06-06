def calculateMarker(n , sprints):
    track = [0] * n


    for i in range(len(sprints) - 1):
        start = sprints[i] - 1
        stop = sprints[i + 1] - 1

        
        if start < stop:
            for j in range(start , stop + 1):
                track[j] = track[j] + 1
        else:
            for j in range(stop , start + 1):
                track[j] = track[j] + 1

    highest_visit = max(track)

    highest_track = track.index(highest_visit) + 1

    return highest_track

print(calculateMarker(5 , [2,4,1,3]))