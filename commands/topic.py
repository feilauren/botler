@command("topic")
def topic(nick, channel, message):
    try:
        import os
        file = open("topic.txt", "r+")
        topic = file.read()
        tempfile = file.read()
        topic = topic.split("\n")
        if message.split()[0] == "add":
            add = str.join(' ', (message.split()[1:]))
            topic.insert(0, add)
            if(os.stat("topic.txt").st_size == 0):
                topic = str.join('', (topic))
            else:
                topic = str.join(' -- ', (topic))
            send('TOPIC {} :{}'.format(channel, topic))
            say(channel, "{}: Topic set.".format(nick))
            file = open("topic.txt", "w")
            topic = topic.split(" -- ")
            topic = str.join("\n", (topic))
            file.write(topic)
        elif message.split()[0] == "file":
            topic = str.join(' -- ', (topic))
            send('TOPIC {} :{}'.format(channel, topic))
            say(channel, "{}: Topic set.".format(nick))
        elif message.split()[0] == "clear":
            file = open("topic.txt", "w")
            send('TOPIC {} :{}'.format(channel, ''))
            say(channel, "{}: Topic set.".format(nick))
        elif message.split()[0] == "remove":
            index = int(message.split()[1])
            index = topic[index]
            topic.remove(index)
            if(os.stat("topic.txt").st_size == 0):
                topic = str.join('', (topic))
            else:
                topic = str.join(' -- ', (topic))
            send('TOPIC {} :{}'.format(channel, topic))
            say(channel, "{}: Topic set.".format(nick))
            file = open("topic.txt", "w")
            topic = topic.split(" -- ")
            topic = str.join("\n", (topic))
            file.write(topic)
        else:
            say(channel, "{}: Invalid input.".format(nick))
    except IndexError:
        say(channel, "{}: Invalid input.".format(nick))
    else:
        pass

    # try:
    #     f = open('topic.txt')
    #     topic = f.read()
    #     topic = topic.split("\n")
    #     topic = str.join(' * ', (topic))
    #     if message.split()[0] == "add":
    #         f = open('topic.txt', 'r+')
    #         newtopic = str.join(' ', (message.split()[1:]))
    #         f.write('{}\n'.format(newtopic))
    #         f.seek(0)
    #         topic = f.read()
    #         topic = topic.split("\n")
    #         topic = str.join(' * ', (topic))
    #         send('TOPIC #mobyte :{}'.format(topic))
    #         say(channel, "{}: Topic set.".format(nick))
    #     elif message.split()[0] == "file":
    #         send('TOPIC #mobyte :{}'.format(topic))
    #         say(channel, "{}: Topic set.".format(nick))
    # except IndexError:
    #     say(channel, "{}: use the format !topic <add|remove|clear> <topic text>".format(nick))
    # else:
    #     pass
