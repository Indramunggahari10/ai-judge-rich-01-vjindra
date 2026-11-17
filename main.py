# ai-judge-rich-01 entry (Python 3.13, standard library only). It writes one fixed
# plan to /output/entry.txt: the plan an AI agent would follow to turn $100, a
# computer with internet access and 30 days, and no human doing the work, into
# the most money. The gate takes UTF-8 text of 1 to 1,000 characters that is
# not only white space; the judge reads exactly the bytes written. The program
# runs twice with no network, and both runs must write the same bytes.
#
# Design: the plan is built to the judge's published criteria in order. Day 1
# verifies the payout rail with a test purchase before any inventory is built,
# so no step rests on a payment that never comes; the rest is a marketplace
# template store with a kill rule, reinvestment, and an untouched reserve.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PARAGRAPHS = (
    "Day 1: open a Gumroad seller account, link payouts to the wallet, and confirm a $1 test purchase clears before building anything. Mine the Discover feed and search suggestions for spreadsheet and planner templates. Rank niches by sales times price divided by competing listings. Pick 3.",
    "Days 2-3: build 6 templates with Python, real formulas, tested. Render preview images in code. List all 6 at $9-$19 with search-written titles. Spend $10 on fees.",
    "Days 4-30: ship one new listing a day. Track views and sales per listing. Kill a niche after 7 days with no sale. Reinvest 80% of revenue into promoting listings with 2+ sales. Keep $30 untouched.",
    "Likely end: 25-30 listings, 3-5 winners, $150-$400 in sales, reserve intact. Edge: while other agents chase trading luck or hunt SaaS customers, these sell to buyers already searching, cost nothing to copy, and compound with every listing.",
)

PLAN = "\n".join(PARAGRAPHS)

# Self-check the gate's shape before writing: 1-1000 code points, not only
# white space. A plan that broke the gate must fail loudly here, never ship.
assert 1 <= len(PLAN) <= 1000 and any(not c.isspace() for c in PLAN)

# Bytes, not text mode: text mode would write the platform's line ends and its
# default encoding. No trailing newline: the judge reads exactly these bytes.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
