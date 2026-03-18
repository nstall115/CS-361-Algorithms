import random
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# PART A
def hybridSort(arr, k):
    # already sorted if there is only 1 element
    if len(arr) <= 1:
        return arr
    
    # chooses insertion if smaller than k
    if len(arr) <= k:
        return insertionSort(arr[:], len(arr))

    # MergeSort
    # divide and conquer from middle
    mid = len(arr) // 2
    sortL = hybridSort(arr[:mid], k) # sort left half
    sortR = hybridSort(arr[mid:], k) # sort right half
    return merge(sortL, sortR)

def insertionSort(arr, n):
    for i in range(1, n):
        key = arr[i] # element that is currently being placed
        # Insert arr[i] into the sorted subarray A[1 : i – 1].
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] # shift to the right
            j -= 1
        # place key
        arr[j + 1] = key
        
    return arr

def merge(left,  right):
    mergeLists = []
    # intialize i and j
    # i = l, r = j, this is to better understand the merge
    l = r = 0 

    # compare left and right side
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            mergeLists.append(left[l])
            l += 1
        else:
            mergeLists.append(right[r])
            r += 1

    mergeLists.extend( left[l:]) # add any leftovers from left
    mergeLists.extend(right[r:]) # add any leftovers from right

    return mergeLists
    
# PART B
# test parameters
sizes  = [100, 1000, 8000]
kVal   = [1, 2, 4, 8, 16, 32, 64]

results = {}   # results[n][k] = avg_ms

print("Run Tests: ")
for n in sizes:
    results[n] = {}
    for k in kVal:
        times = []
        i = 0
        # collect indivdual runtimes of each trail
        while i != 5:                                    # run 5 times
            arr = random.sample(range(1, n * 10 + 1), n) # random array
            start = time.perf_counter()
            hybridSort(arr, k)
            end = time.perf_counter()
            times.append((end - start) * 1000)           # convert to ms
            i += 1
        # average runs
        avg_ms = sum(times) / 5
        results[n][k] = avg_ms
        print(f"n ={n:>5}, k ={k:>3} avg: {avg_ms:.4f} ms")

# print outcomes
print("\nOptimal k values:")
optimal = {}
for n in sizes:
    bestK = min(results[n], key=results[n].get)
    optimal[n] = bestK
    print(f"n ={n:>5}: Best K value: {bestK} at {results[n][bestK]:.4f} ms")

# q4
# plot outcomes
COLORS  = ["#E63946", "#2A9D8F", "#F4A261"]
MARKERS = ["o", "s", "^"]

fig, ax = plt.subplots(figsize=(9, 5.5))
fig.patch.set_facecolor("#0F1117")
ax.set_facecolor("#0F1117")

# iterate over each array and draw one line per size
for idx, n in enumerate(sizes):
    y = [results[n][k] for k in kVal] # k runtime at n
    ax.plot(
        kVal, y,
        color=COLORS[idx],
        marker=MARKERS[idx],
        linewidth=2,
        markersize=7,
        label=f"n = {n:,}",
    )
    # Mark the optimal k with a star
    best_k  = optimal[n]
    best_ms = results[n][best_k]
    ax.plot(best_k, best_ms, "*", color=COLORS[idx], markersize=14, zorder=5)

ax.set_xscale("log", base=2)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x)}"))
ax.set_xticks(kVal)

for spine in ax.spines.values():
    spine.set_edgecolor("#333344")

ax.tick_params(colors="#AAAACC", labelsize=10)
ax.set_xlabel("Threshold k  (subarray size -> insertion sort)", color="#CCCCDD", fontsize=12)
ax.set_ylabel("Average runtime (ms)", color="#CCCCDD", fontsize=12)
ax.set_title ("Hybrid Sort Performance: Merge + Insertion Sort", color="white", fontsize=14, pad=14)

legend = ax.legend(
    title="Array size  (★ = optimal k)",
    title_fontsize=9,
    fontsize=10,
    facecolor="#1A1A2E",
    edgecolor="#333344",
    labelcolor="#DDDDEE",
)
legend.get_title().set_color("#AAAACC")

ax.grid(True, which="major", linestyle="--", linewidth=0.5, color="#2A2A3A", alpha=0.8)

plt.tight_layout()
plt.show()