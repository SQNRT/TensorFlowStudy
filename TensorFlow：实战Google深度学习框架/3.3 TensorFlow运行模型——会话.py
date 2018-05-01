import tensorflow as tf

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = a + b

sess = tf.Session()
with sess.as_default():
    print(result.eval())

print(sess.run(result))
print(result.eval(session=sess))

sess = tf.InteractiveSession()
print(result.eval())
sess.close()

config = tf.ConfigProto(allow_soft_placement = True, log_device_placement = True)
sess1 = tf.InteractiveSession(config=config)
sess2 = tf.Session(config=config)