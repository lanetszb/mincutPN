import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import rc

rc('text', usetex=True)

fig_width = 3.5

table = pd.read_csv('perm_comparison_1.csv') 
df = pd.DataFrame(table) 

df = df.sort_values(by=['k_pnm'])     
df.index = df.k_pnm

def implement_filter(table, threshold, remove_rate):
    remove_n = int(len(table.index[table.index < threshold]) * remove_rate)    
    drop_indices = np.random.choice(table.index[table.index < threshold], remove_n, replace=False)

    return table.drop(drop_indices)

df = implement_filter(df, 3.e-12, 0.5)
df = implement_filter(df, 1.e-12, 0.7)
df = implement_filter(df, 5.e-12, 0.3)

# Plot 1
ax1 = df.plot(x='k_pnm', y='k_edm', figsize=(fig_width, fig_width), style='o', label = 'Artificial', legend=False, zorder=1)

k_min = 5.e-14
k_max = 1.25e-11
                                    
                         
ax1.set_xlim(k_min, k_max)                                                                                        
ax1.set_ylim(k_min,k_max)                                                                         
                      
ax1.set_xlabel("$k_{pnm}$")     
ax1.set_ylabel("$k_{edm}$")                                                                        
                     

                  
plt.gca().set_aspect('equal', adjustable='box')                                                        
plt.plot([k_min,k_max], [k_min,k_max])     

# plt.scatter(4.194141E-10, 3.555365E-10, c="r", alpha=1, marker='square', label='Silica', zorder=2)    
plt.scatter(2.298116E-13, 1.889883E-13, c="cyan", alpha=1, marker='s', label='Castle',zorder=2, s = 50)    
plt.scatter(3.622896E-12, 1.487646E-12, c="m", alpha=1, marker='s', label='Gambier', zorder=2, s = 50)       
plt.scatter(1.067776E-11, 1.013048E-11, c="r", alpha=1, marker='s', label='Bead Pack', zorder=2, s = 50)    
    
plt.legend()  
  
plt.savefig("k_pnm_edm.eps", format="eps", bbox_inches = 'tight')  
                                                                                             
plt.show() 


# Plot 2
df['error_rel'] = (df.k_pnm - df.k_edm) / df.k_pnm

ax2 = df.plot(x='k_pnm', y='error_rel', figsize=(fig_width, fig_width*1.1), style='o', label = 'Artificial', legend=True, zorder=1)     
                             

mean_err = df.error_rel.mean()
plt.plot([k_min,k_max], [mean_err,mean_err])
                                                                                                                           
ax2.set_xlim(k_min,k_max)    
ax2.set_ylim(-0.3,0.8)      
      
ax2.set_xlabel("$k_{pnm}$")     
ax2.set_ylabel("Relative error")                                   

# plt.scatter(4.194141E-10, (4.194141E-10 - 3.555365E-10) / 4.194141E-10, c="r", alpha=1, marker='square', label='Silica', zorder=2)    
plt.scatter(2.298116E-13, (2.298116E-13 - 1.889883E-13) / 2.298116E-13, c="cyan", alpha=1, marker='s', label='Castle', zorder=2, s = 50)    
plt.scatter(3.622896E-12, (3.622896E-12 - 1.487646E-12) / 3.622896E-12, c="m", alpha=1, marker='s', label='Gambier', zorder=2, s = 50)       
plt.scatter(1.067776E-11, (1.067776E-11 - 1.013048E-11) / 1.067776E-11, c="r", alpha=1, marker='s', label='Bead Pack', zorder=2, s = 50)  

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)
                                           
                                                                                          

 
plt.savefig("error_rel.eps", format="eps", bbox_inches = 'tight')  
                                                                                              
plt.show() 

