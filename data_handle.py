def load_data( filepath ):
    #filepath = '/home/scu/datasets/ILSVRC2013/LSDL_Data/misvm_data/ss_tmp_train_bin_classify_cat_1.data'
    filein = open(filepath, 'r')
    FEAT_DIM = 4096
    bags = []
    labels = []
    bagNow = 0
    bag = []
    label = -1
    count = 0
    for line in filein:
        count += 1
        data = line.split(',')
        #instID = data[0]
        bagProcess = data[1]
        bagName = "Bag" + str(bagNow)
        if(bagName != bagProcess):
            bagNow = bagNow + 1
            bagName = "Bag" + str(bagNow)
            if count != 1:
                bags.append(bag)
                #bag insert into the list at the end
            bag = []
            label = 2 * int(data[2]) - 1
            labels.append(label) 
            #label insert in the list at the beginning
            #since the representative label is the first instance
        sparse_feat_len = len(data)
        feats = [0] * FEAT_DIM
        for i in range(3, sparse_feat_len):
            feat = data[i].split(':')
            feat_id = int(feat[0])
            feat_val = float(feat[1])
            feats[feat_id-1] = feat_val
        bag.append(feats);
    bags.append(bag) 
    #bag insert into the list at the end for the last iteration!
    filein.close()
    summ = 0.0
    for i in range(0, len(bags)):
        summ += len( bags[i] )
        print "bags[%d] has %d instances" % (i,len( bags[i]))
    print "average instances in a bag: %f\ntotal instances: %d" % (summ/len(bags), summ)
    print labels
    
    return [bags, labels]
