from nifs3 import get_s
import data
import matplotlib.pyplot as plt

sx1 = get_s(data.ts1, data.xs1)
sy1 = get_s(data.ts1, data.ys1)
plt.plot([sx1(u) for u in data.us1], [sy1(u) for u in data.us1])

sx2 = get_s(data.ts2, data.xs2)
sy2 = get_s(data.ts2, data.ys2)
plt.plot([sx2(u) for u in data.us2], [sy2(u) for u in data.us2])

sx3 = get_s(data.ts3, data.xs3)
sy3 = get_s(data.ts3, data.ys3)
plt.plot([sx3(u) for u in data.us3], [sy3(u) for u in data.us3])

sx4 = get_s(data.ts4, data.xs4)
sy4 = get_s(data.ts4, data.ys4)
plt.plot([sx4(u) for u in data.us4], [sy4(u) for u in data.us4])

plt.xlim(0.0, 180.0)
plt.ylim(-4, 20.0)
plt.show()

