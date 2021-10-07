import heapq

def solution(operations):

    inputs = []
    input_counter = 0
    min_heap = []
    max_heap = []
    counter = 0

    for op_idx in range(len(operations)):
        # input
        if operations[op_idx][0] == "I":

            inp = int(operations[op_idx][2:])
            counter += 1

            inputs.append(inp)
            heapq.heappush(min_heap, (inp, input_counter))
            heapq.heappush(max_heap, (-inp, input_counter))
            input_counter += 1

        if operations[op_idx][0] == "D":
            if counter:
                counter -= 1

                # del min
                if operations[op_idx][2] == "-":
                    # delete pre_deleted
                    pre_deleted = True

                    while pre_deleted:
                        if inputs[min_heap[0][1]] is None:
                            heapq.heappop(min_heap)
                        else:
                            pre_deleted = False

                    _, del_idx = heapq.heappop(min_heap)
                    inputs[del_idx] = None
                # del max
                else:
                    # delete pre_deleted
                    pre_deleted = True

                    while pre_deleted:
                        if inputs[max_heap[0][1]] is None:
                            heapq.heappop(max_heap)
                        else:
                            pre_deleted = False

                    _, del_idx = heapq.heappop(max_heap)
                    inputs[del_idx] = None

    answer_arr = [_ for _ in inputs if _ is not None]
    if len(answer_arr):
        return [max(answer_arr), min(answer_arr)]
    else:
        return [0,0]


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))