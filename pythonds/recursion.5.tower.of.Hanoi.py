# http://interactivepython.org/runestone/static/pythonds/Recursion/TowerofHanoi.html
# 
# a little imporvement to add list of # of tower

def moveTower(listDisk, fromPole, toPole, withPole):
    if len(listDisk):
        moveTower(listDisk[1:], fromPole, withPole, toPole)

        # move the bottom Disk from fromPole to toPole
        moveDisk(listDisk[0], fromPole, toPole)

        moveTower(listDisk[1:], withPole, toPole, fromPole)

def moveDisk(nameDisk, fromPole, toPole):
    print "moving disk -", nameDisk, 'from', fromPole, 'to', toPole


print '!!! moving 4321 from A to B by using C'
moveTower('842', 'A', 'B', 'C')
