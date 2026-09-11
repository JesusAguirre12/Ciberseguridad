s = "jU5t_a_sna_3lpm13g64f_u_4_m6r143"

ans = ["_"]*len(s)

for i in range(8):
    ans[i]=s[i]
    
for i in range(8,16):
    ans[23-i]=s[i]
   
for i in range(16,32,2):
   ans[46-i]=s[i]

for i in range(31, 16, -2):
   ans[i]=s[i]
   
print(f"picoCTF{{{"".join(ans)}}}")
