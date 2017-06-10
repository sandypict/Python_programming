
def tuner(**kargs):
    print kargs

tuner()
tuner(contrast=0.8, hue=0.3)


# Following is example of sending dictionary as an argument to keyword function

items=dict(name='larry', age=7)
tuner(**items)

def cat(file_name, **kwargs):
    reverse2 = kwargs.get('reverse1', False)
    content = open(file_name,).readlines()

    if reverse2:
        content.reverse()
    for line in content:
        print line,

#cat('C:/Users/chavas5/PycharmProjects/untitled/a.txt')
print \
cat('C:/Users/chavas5/PycharmProjects/untitled/a.txt',reverse1=True)