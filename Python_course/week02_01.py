import argparse
import os
import tempfile
import json

#
parser = argparse.ArgumentParser()
# parser.add_argument("--key", nargs='*', action='append')
# parser.add_argument("--val", nargs='*', action='append')
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#storage_path = 'storage.data'
try:
    f = open(storage_path, 'r+')
except FileNotFoundError:
    f = open(storage_path, 'w+')
try:
    ans = json.load(f)
except json.decoder.JSONDecodeError:
    ans = {}

if args.val:
    try:
        ans[args.key].append(args.val)
    except KeyError:
        ans[args.key] = [args.val]
else:
    try:
        print(*ans[args.key], sep=", ")
    except KeyError:
        print("")
# if len(args.key) == len(args.val):
#     for x in zip(args.key, args.val):
#         for key in x[0]:
#             if not ans[key]:
#                 ans[key] = x[1]
#             else:
#                 ans[key] += x[1]
# elif args.val:
#     if not ans[args.key[0]]:
#         ans[args.key[0]] = args.val
#     else:
#         ans[args.key[0]] += args.val
# else:
#     for key in args.key:
#         if ans[key]:
#             print(*ans[key], sep=", ")
#         else:
#             print("")
f = open(storage_path, 'r+')
json.dump(ans, f)
f.close()
