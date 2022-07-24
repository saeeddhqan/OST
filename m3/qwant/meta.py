import q
import et


def simple_merge(results):
	engines_len = len(results)
	merged = []

	for i in range(len(min(results, key=len))):
		for e in range(engines_len):
			merged.append(results[e%engines_len].pop(0))

	for i in results:
		for j in i:
			merged.append(j)

	return merged

def remove_dups(results):
	pass


results1 = q.run('heat')
results2 = et.run('heat')

final_results = [results1, results2]
merged = simple_merge(final_results)

for i in merged:
	print(i['url'])
	print(i['title'])
	print(i['text'])
	print()
