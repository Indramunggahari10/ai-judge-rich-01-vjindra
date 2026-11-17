# ai-judge-rich-01 entry — vjindra account

A program that writes one plan to `/output/entry.txt`: the plan an AI agent
would follow starting with $100, internet access and 30 days, and no human
doing the work, to end with the most money.

The plan: verify the payout rail on day 1, then sell spreadsheet and planner
templates on a marketplace that already brings the buyers — one new listing a
day, kill rules for dead niches, revenue reinvested into proven winners, and a
$30 reserve kept untouched.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program is deterministic: two runs write identical bytes, no network.
