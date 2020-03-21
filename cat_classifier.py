import os
import torch
from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms


__all__ = ('CatPipeline',)


class ImagesDataset(Dataset):
    def __init__(self, fold):
        self.file_list = os.listdir(fold)
        self.fold = fold
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        img = Image.open(os.path.join(self.fold, self.file_list[idx]))

        if self.transform:
            img = self.transform(img)
            result = {}
            result['filenames'] = self.file_list[idx]
            result['img'] = img
            return result


class CatPipeline:
    def __init__(self, device='cpu'):
        self.model = torch.hub.load('pytorch/vision:v0.5.0', 'mobilenet_v2', pretrained=True)
        self.model.eval().to(device)
        self.device = device

    def run(self, folder):
        testset = ImagesDataset(folder)
        testloader = DataLoader(testset, batch_size=8, shuffle=False, num_workers=8)
        result = {}

        for batch in testloader:
            output = self.model(batch['img'].to(self.device))
            label = torch.argmax(output, dim=1).cpu().numpy()
            decode_label = []
            for ind, l in enumerate(label):
                if l in [281, 282, 283, 284, 285, 383, 286, 287, 288]:
                    decode_label.append(True)
                else:
                    decode_label.append(False)

            result.update(dict(zip(batch['filenames'], decode_label)))

        return result
