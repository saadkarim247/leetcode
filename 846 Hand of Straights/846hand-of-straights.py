class Solution:
    def isNStraightHand(self, hand: List[int], g: int) -> bool:
        hand.sort()

        flag = True
        if len(hand) % g != 0:
            # print("testing")
            return False
        else:
            if (g == 1):
                return True
            else:
                while (hand and flag):
                    x = hand[0]
                    for i in range(1, g):
                        if (x + i) in hand:
                            if (i == g-1):
                                hand.remove(x)
                            hand.remove(x+i)
                            continue
                        else:
                            flag = False
                            return False
                            break
                    if (not hand):
                        return True
