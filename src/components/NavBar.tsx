import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "./ui/dropdown-menu";

export default function NavBar() {
  return (
    <div className="w-screen px-8">
      <div
        className="flex justify-between w-full p-4 px-8 border border-white rounded-xl"
        // style={{ width: "100vw" }}
      >
        {/* Replace this with image when i get that chance to make a logo */}
        <h1 className="flex items-center justify-start text-small font-bauer">
          Breakout Zone
        </h1>
        <div className="flex items-center">
          <DropdownMenu>
            <DropdownMenuTrigger>Select Versus</DropdownMenuTrigger>
            <DropdownMenuContent>
              <DropdownMenuLabel>My Account</DropdownMenuLabel>
              <DropdownMenuSeparator />
              <DropdownMenuItem>1 v 1</DropdownMenuItem>
              <DropdownMenuItem>Team v Team</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>
    </div>
  );
}
