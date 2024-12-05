select W1.id
from weather W1
inner join weather W2
    on W1.recorddate=W2.recorddate+1
where W1.temperature>W2.temperature