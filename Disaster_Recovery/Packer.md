# AMI - Amazon Machine Image with packer
An Amazon Machine Image (AMI) is a pre-configured virtual machine image, which is used to create Amazon Elastic Compute Cloud (EC2) instances (virtual servers) within the Amazon Web Services (AWS) environment. An AMI contains the necessary information to launch an instance, including the operating system, application server, and applications.

These are images for virtual machine such as EC2.  Different from docker images for containers. 

## Packer
We use packer to build these images. 
Packer is an open-source tool developed by HashiCorp that allows you to automate the creation of machine images for multiple platforms, including Amazon Machine Images (AMIs) for AWS. 
Using Packer, you can define the configuration of your machine image in a template file, and Packer will then create the image for you. Here's a basic guide on how to use Packer to build an AMI:

## Steps
1. Install Packer:
Make sure you have Packer installed on your machine. You can download it from the official website: https://www.packer.io/downloads

2. Create a Packer Template:
Create a JSON file that describes the configuration of your AMI. This file is known as the Packer template. Here is a simple example template for an AWS AMI:

```
{
  "builders": [
    {
      "type": "amazon-ebs",
      "region": "your-aws-region",
      "source_ami": "source-ami-id",
      "instance_type": "t2.micro",
      "ssh_username": "ubuntu",
      "ami_name": "my-custom-ami-{{timestamp}}"
    }
  ]
}
```
Customize the template according to your requirements. You need to specify the AWS region, source AMI ID, instance type, SSH username, and other parameters.

3. Run Packer Build:
Open a terminal and navigate to the directory containing your Packer template. 
Run the following command to build your AMI:
```
packer build your-template.json
```

4. Wait for the Build to Complete:
Packer will launch a temporary EC2 instance, provision it based on your template, and then create a new AMI. The process may take some time, depending on the complexity of your configuration and the time it takes to provision the instance.

5. Review the AMI:
Once the build is complete, Packer will output information about the created AMI, including the AMI ID. You can find the new AMI in the AWS Management Console.