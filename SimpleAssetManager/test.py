from AssetList import AssetList

a = AssetList()

a.AddAsset("test")
a.UpdateAsset(2,"name","super")
a.RemoveAsset([3,4,5,6])
#a.PrintAllAssets()
print(a.GetAllAssets())
