namespace FullStackCSharp.Front;

public partial class MainPage : ContentPage
{
	int count = 0;

	public MainPage()
	{
		InitializeComponent();
	}

	private void OnCounterClicked(object? sender, EventArgs e)
	{
		count++;

		if (count == 1)
		CounterBtn.Text = $"Interaction validée : {count} clic";
		else
		CounterBtn.Text = $"Interaction validée : {count} clics";

		SemanticScreenReader.Announce(CounterBtn.Text);
	}
}
