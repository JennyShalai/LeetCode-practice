def merge(intervals):
  if len(intervals) < 2:
    return intervals

  # sorting intervals in incrising order
  intervals.sort()
    
  # merging sorted intervals
  end = -1
  result = []
  for i in sortedIntervals:
    currStart = i[0]
    currEnd = i[1]
    if currStart <= end:
      currEnd = max(currEnd,result[-1][1])
      result[-1][1] = currEnd
      end = currEnd
    else:
      result.append(i)
      end = currEnd
  return result   

print( merge ([[1,4],[0,4]]) ) # [[0,4]]
print( merge ([[1,4],[2,3]]) ) # [[1,4]]
print( merge ([[2,3],[4,5],[6,7],[8,9],[1,10]]) ) # [[1,10]]
print( merge ([[2,3],[5,5],[2,2],[3,4],[3,4]]) ) # [[2,4],[5,5]]
