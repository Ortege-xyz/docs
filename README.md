# README
Our Quarto based documentation

## Running locally
### Install Quarto
First, ensure you have Quarto installed. If you haven't installed Quarto yet, you can download it from the official Quarto website and follow the installation instructions for your operating system.

### Serve the Quarto website locally
Open a Terminal or Command Prompt: Navigate to the root directory of your Quarto project where your _quarto.yml and content files are located.

Serve the Website: Run the following command to serve your Quarto website locally:

`quarto serve`

This command starts a local web server and automatically opens your default web browser to the address of your locally served site (usually http://localhost:4000 or similar). If the browser doesn't open automatically, you can manually open it and enter the local address provided in the terminal output.

## Publishing
Just run `quarto publish`

This is a self documenting document repo. Please go to the `index.qmd` to read about our documention. 

## Updating the Lakehouse schema's
`DESCRIBE TABLE external.db_stacks.tbl_dev_br_blocks`