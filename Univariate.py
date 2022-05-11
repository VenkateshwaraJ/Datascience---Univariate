class univariate():
    

    def QuanQual(self,dataset):
        Quan=[]
        Qual=[]
        for columnname in dataset.columns:
            print(columnname)
            if(dataset[columnname].dtypes=="O"):
                #print("Qual")
                Quan.append(columnname)
            else:
                #print("Quan")
                Qual.append(columnname)
        return Quan,Qual