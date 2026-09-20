# Edge Case & Error Analysis - Grade Processing Tool

## Overview
This document explains error handling for grade_checker.py which calculates weighted marks: Practical (40%) + Theory (60%).

## Invalid Input Cases

### Case 1: Text input like "abc"
- **Input Example:** User types "abc" when asked for Practical mark
- **Error Category:** Runtime Error (ValueError)
- **Explanation:** The program calls float() to convert input. float("abc") fails during execution because "abc" cannot be converted to a number. This is not a syntax error because code is written correctly, it only fails at runtime with bad data.
- **Impact without handling:** Program crashes with traceback and stops.

### Case 2: Out-of-range number like 150
- **Input Example:** User enters 150 for Theory mark
- **Error Category:** Semantic / Logic Error
- **Explanation:** 150 is a valid float, so no runtime error occurs. However, marks must logically be 0-100. Allowing 150 would cause incorrect weighted calculation and wrong PASS/FAIL decision. This is a logic flaw, not a code crash.
- **Impact without handling:** Incorrect final percentage and incorrect pass/fail result.

## Prevention Methods

1. **Type Casting with float() + try/except:**
   - float() attempts conversion
   - try/except ValueError catches Runtime Error from "abc"
   - Shows friendly message: "Please enter valid numbers only"
   - Prevents system crash

2. **Explicit Range Validation:**
   - if not (0 <= practical <= 100) or not (0 <= theory <= 100):
   - Catches Semantic/Logic errors like 150 or -10
   - Stops incorrect logic execution before calculation
   - Ensures data integrity and correct threshold check (50%)

Together they ensure stability and correctness.
