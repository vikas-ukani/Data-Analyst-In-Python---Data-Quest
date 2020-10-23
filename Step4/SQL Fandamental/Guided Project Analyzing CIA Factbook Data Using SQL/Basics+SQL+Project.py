#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('conda install -yc conda-forge ipython-sql')


# In[3]:


get_ipython().run_cell_magic('capture', '', '%load_ext sql\n%sql sqlite:///factbook.db')


# In[6]:


get_ipython().run_cell_magic('sql', '', "SELECT *\n  FROM sqlite_master\n WHERE type='table';")


# In[8]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\n  FROM facts\nLIMIT 5;\n\n ')


# In[11]:



get_ipython().run_cell_magic('sql', '', 'SELECT\n\nMIN(population ),\nMIN(population ),\n\n\nMIN(population_growth ),\nMIN(population_growth )\n\n\n  \n    FROM facts\n\n \n')


# In[14]:


get_ipython().run_cell_magic('sql', '', 'SELECT\nname, \nmin(population )\n\nfrom facts\nGroup by name')


# In[16]:



get_ipython().run_cell_magic('sql', '', 'SELECT\nname, \nmax(population )\n\nfrom facts\nGroup by name')


# In[17]:




get_ipython().run_cell_magic('sql', '', 'SELECT avg(population) , avg(area) from facts')


# In[18]:




get_ipython().run_cell_magic('sql', '', 'SELECT\navg(population\nfrom facts where population > (select avg(avg_pop) from facts)')


# In[ ]:




