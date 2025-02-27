# OUMSSA-Election-AntiFraud-Mechanism

## Stage 1: Qualtrics
Qualtrics is very intuitive to use: create an account and make your form using a ranked choice list

You need to create a contact list using all OUMSSA members in order to generate the unique voter link

Also, put in a question that takes in a voter ID as input, and validates it against a regex pattern to your liking (I suggest 10 character strings with some further structure imposed)

Some things to test: 
1. Test the validation of IDs
2. Test that you can only use your own link once
3. Try to use someone else's link after they have already voted

## Stage 2: Voter ID
Generate a voter ID with at least 8 characters that satisfies a specific regex pattern that you should not disclose before the election 

The Voter ID generation script helps you generate the IDs instantly

The Verification script is a first-instance test for the voter IDs, to give you a prima facie impression over whether fraud has been conducted. 
