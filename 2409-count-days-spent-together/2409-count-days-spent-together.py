class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        aliceArrivalDays = sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:int(arriveAlice.split('-')[0]) - 1]) + int(arriveAlice.split('-')[1])
        aliceLeavingDays = sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:int(leaveAlice.split('-')[0]) - 1]) + int(leaveAlice.split('-')[1])

        bobArrivalDays = sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:int(arriveBob.split('-')[0]) - 1]) + int(arriveBob.split('-')[1])
        bobLeavingDays = sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:int(leaveBob.split('-')[0]) - 1]) + int(leaveBob.split('-')[1])

        if (aliceLeavingDays < bobArrivalDays or bobLeavingDays < aliceArrivalDays):
            return 0
        latestArrival = aliceArrivalDays if aliceArrivalDays > bobArrivalDays else bobArrivalDays
        if aliceLeavingDays < bobLeavingDays:
            return aliceLeavingDays-latestArrival + 1
        else:
            return bobLeavingDays-latestArrival + 1


