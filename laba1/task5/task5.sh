touch ex5.txt

chmod 666 ex5.txt

ls -la ex5.txt >> ex5.txt

chmod 707 ex5.txt

ls -la ex5.txt >> ex5.txt

chmod "$(stat --format '%a' ex5.txt | cut -c1)""$(stat --format '%a' ex5.txt | cut -c1)""$(stat --format '%a' ex5.txt | cut -c3)" ex5.txt

ls -la ex5.txt >> ex5.txt